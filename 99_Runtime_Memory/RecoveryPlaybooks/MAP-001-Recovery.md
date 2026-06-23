Map停止時確認順序

1.
PrimaryMapRenderer mount

2.
displayData

3.
cache[dateKey]

4.
setCache

5.
precomputeMapData

6.
loadGoogleMaps

7.
getGoogleMapsApiKey

正常版:
17477ae1

注意:
CommandRuntimeを犯人扱いしない
