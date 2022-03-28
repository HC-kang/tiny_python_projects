import os

os.mkdir('lower')
for file in os.listdir('.'):
    fh = open(file)
    out = open(os.path.join('./lower', file), 'wt')
    for line in fh:
        out.write(line.lower())
    fh.close()
    out.close()