kody, root, p = [list(ln) for ln in [line.strip() for line in open("ciarovy_kod_1.txt").readlines()]], __import__("tkinter").Tk(), globals().update(kody_i = 0)
c = __import__("tkinter").Canvas(root, width="500", height="500")
c.pack()
def render(kod, off_x, off_y):
    for i in range(len(kod)):
        if i > 0 and i < 7: c.create_line(10 + off_x + 10 * i, 0 + off_y, 10 + off_x + 10 * i, 60 + off_y, width=kod[i])
        else: c.create_line(10 + off_x + 10 * i, 0 + off_y, 10 + off_x + 10 * i, 80 + off_y, width=kod[i])
    c.create_text(45 + off_x, 70 + off_y, text="".join(kod))
def render4(): [c.delete("all"), render(kody[kody_i], 0, 0), render(kody[kody_i+1], 120, 0), render(kody[kody_i+2], 0, 100), render(kody[kody_i+3], 120, 100), globals().update(kody_i = kody_i + 4)]
[root.bind("<space>", lambda _: render4()), root.mainloop()]