import pyupbit

access = "0zThBjho5AAr9C4XSyd2fwwTL34vopx7nI8cBYZJ"          # 본인 값으로 변경
secret = "XzxxzgVnW03bd6Tj64xDwZb1gA9o75QMz5DPWzmV"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

