from typing import Union, Any, cast, Dict, Callable
from datetime import datetime
import os, re, pickle, codecs, gzip, hashlib
import time

_deserializeCache: Dict[str, Any] = {}


# From https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size
def sizeOfFmt(num: Union[int, Any]):
  if type(num) != int:
    return ""
  numLeft: float = num
  for unit in ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB"]:
    if abs(numLeft) < 1000.0:
      return f"{numLeft:3.0f} {unit}"
    numLeft /= 1000.0
  return f"{numLeft:.1f} YB"


def pandasTypeToPythonType(pandasType: str):
  if pandasType in ['float32', 'float64']:
    return 'float'
  if pandasType in ['int32', 'int64']:
    return 'int'
  if pandasType == 'bool':
    return 'bool'
  return 'Any'


def simplifyArgName(argName: str):
  scrubbed = re.sub("\\W+", "_", argName.lower())
  scrubbed = re.sub('^(\\d+)', "c\\1", scrubbed)
  if scrubbed.endswith("_"):
    scrubbed = scrubbed[:-1]
  return scrubbed


def unindent(source: str) -> str:
  leadingWhitespaces = len(source) - len(source.lstrip())
  if leadingWhitespaces == 0:
    return source
  newLines = [line[leadingWhitespaces:] for line in source.split("\n")]
  return "\n".join(newLines)


def timeago(pastDateMs: int):
  nowMs = time.time() * 1000
  options = [
      {
          "name": "second",
          "divide": 1000
      },
      {
          "name": "minute",
          "divide": 60
      },
      {
          "name": "hour",
          "divide": 60
      },
      {
          "name": "day",
          "divide": 24
      },
      {
          "name": "month",
          "divide": 30.5
      },
  ]
  currentDiff = nowMs - pastDateMs
  if currentDiff < 0:
    raise Exception("The future is NYI")
  resp = "Just now"
  for opt in options:
    currentDiff = round(currentDiff / cast(Union[float, int], opt["divide"]))
    if currentDiff <= 0:
      return resp
    pluralS = ""
    if currentDiff != 1:
      pluralS = "s"
    resp = f"{currentDiff} {opt['name']}{pluralS} ago"
  return resp


def deprecated_unpickleObj(str64: str):
  return pickle.loads(codecs.decode(str64.encode(), "base64"))


def deprecated_pickleObj(obj: Any):
  return codecs.encode(pickle.dumps(obj), "base64").decode()


def deserialize(contentHash: str, reader: Callable[..., Any]):
  if contentHash not in _deserializeCache:
    _deserializeCache[contentHash] = pickle.loads(gzip.decompress(reader()))
  return _deserializeCache[contentHash]


def serialize(obj: Any):
  pklData = pickle.dumps(obj)
  zippedPickle = gzip.compress(pklData, compresslevel=1)
  contentHash = hashlib.md5(pklData).hexdigest()
  return (zippedPickle, contentHash)


def timestamp():
  return int(datetime.timestamp(datetime.now()) * 1000)


def getEnvOrDefault(key: str, defaultVal: str) -> str:
  osVal = os.getenv(key)
  if type(osVal) == str:
    return str(osVal)
  else:
    return defaultVal
