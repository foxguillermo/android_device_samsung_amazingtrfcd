

elines = {}
for l in open("extract-files.sh","r").readlines():
    if ("#" in l):
        continue
    if ("mkdir" in l):
        continue
    if "" == l.strip():
        continue
    ls = l.split(" ")
    if len(ls) < 2:
        continue
    libname = ls[2]
    ll = libname.split("/")
    if len(ll) > 1:
        libname = libname[-1]
        elines[libname] = libname

slines = {}
for l in open("system_libs","r").readlines():
    libname = l.strip()
    slines[libname] = libname

all_libs = {}
for e in elines.keys():
    if slines.has_key(e):
        all_libs[e] = e

for e in slines.keys():
    all_libs[e] = e

print all_libs.keys()

f = open("all_libs","w")
ks = all_libs.keys()
ks.sort()
for k in ks:
    f.write("%s\n" % k)
f.close()
