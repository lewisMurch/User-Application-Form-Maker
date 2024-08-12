import re

text = """
uid=10001(abc123) gid=10001(abc123) groups=10001(abc123)
uid=10002(def456) gid=10002(def456) groups=10002(def456)
uid=10003(ghi789) gid=10003(ghi789) groups=10003(ghi789)
uid=10004(jkl012) gid=10004(jkl012) groups=10004(jkl012)
uid=10005(mno345) gid=10005(mno345) groups=10005(mno345)
uid=10006(pqr678) gid=10006(pqr678) groups=10006(pqr678)
uid=10007(stu901) gid=10007(stu901) groups=10007(stu901)
uid=10008(vwx234) gid=10008(vwx234) groups=10008(vwx234)
uid=10009(yza567) gid=10009(yza567) groups=10009(yza567)
uid=10010(bcd890) gid=10010(bcd890) groups=10010(bcd890)
"""


# Extract UID numbers
uid_numbers = re.findall(r'uid=(\d+)', text)

# Print each UID on a new line
for uid in uid_numbers:
    print(uid)
