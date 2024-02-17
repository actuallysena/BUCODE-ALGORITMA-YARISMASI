def rukiyenin_Cicekleri(n, m, x, y, k, cicekler):
  sulandi = set()

  def sulanan_alan(x, y, uzaklik):
    for i in range(-uzaklik, uzaklik+1):   
        #yukari
        if 0 <= x + i <= n and 0 <= y - uzaklik <= m:
          if (x + i, y - uzaklik) in cicekler:
            sulandi.add((x + i, y - uzaklik))
        #asagi
        if 0 <= x + i <= n and 0 <= y + uzaklik <= m:
          if (x + i, y + uzaklik) in cicekler:
            sulandi.add((x + i, y + uzaklik))
        #sol
        if 0 <= x - uzaklik <= n and 0 <= y + i <= m:
          if (x - uzaklik, y + i) in cicekler:
            sulandi.add((x - uzaklik, y + i))
        #sağ
        if 0 <= x + uzaklik <= n and 0 <= y + i <= m:
          if (x + uzaklik, y + i) in cicekler:
            sulandi.add((x + uzaklik, y + i))

  uzaklik = 1
  while uzaklik <= max(n, m):
    sulanan_alan(x, y, uzaklik)
    uzaklik += 2


  sulanan_cicekler = len(sulandi)
  return sulanan_cicekler



n, m, k = map(int, input().split())
x, y = map(int, input().split())

cicekler = []
for i in range(k):
  cicek_x, cicek_y = map(int, input().split())
  cicekler.append((cicek_x, cicek_y))

print(rukiyenin_Cicekleri(n, m, x, y, k, cicekler))

