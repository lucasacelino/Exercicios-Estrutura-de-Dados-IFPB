def sistemaCalibrePneus(pressaDesejada, totalPneusDescalibrados):
    pressaDesejada = totalPneusDescalibrados[0]
    subValores = [pressaDesejada - sub for sub in totalPneusDescalibrados[1:]]
    qtdPneusDescalibrados = len(totalPneusDescalibrados[1:])
    subValores.insert(0, qtdPneusDescalibrados)
    return subValores

calibrePneus = list(map(int, input().split()))
pressaDesejada = calibrePneus[0]
while(calibrePneus[0] != 0):
    resultCalibres = sistemaCalibrePneus(pressaDesejada, calibrePneus)
    for calibre in resultCalibres:
        print(calibre, end=' ')
    print()
    calibrePneus = list(map(int, input().split()))