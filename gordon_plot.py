import matplotlib.pyplot as plt

def gordon(d0, g, r):
#Gordon growth model/ Divident discount model

    if r>g:
        d1 = d0*(1+(g/100))
        p = d1/((r-g)/100)
        return round(p, 2)
    return 0

d0 = 64

#print(gordon(13, 4, 9))

x = list(range(4, 10))  #g

matrix = []
r_list = [8, 9, 10]
for r in r_list:
    row = []
    for num in x:
        p = gordon(d0, num, r)
        row.append(p)
    matrix.append(row)

print(matrix)

labels = []
for r in r_list:
    label = "r = " + str(r)
    labels.append(label)

#print(labels)

plt.plot(x, matrix[0], label= labels[0], color="blue", linestyle="-", marker="o")
plt.plot(x, matrix[1], label= labels[1], color="green", linestyle="-", marker="o")
plt.plot(x, matrix[2], label= labels[2], color="red", linestyle="-", marker="o")


plt.title("Gordon Growth Model using TCS as Case Study")
plt.xlabel("Dividend Growth Rate(g) %")
plt.ylabel("Instrinsic value (P) in Rupees")
plt.text(3.85, 5166, "D1 = Expected Dividend per Share ", fontsize=12, color="black")
plt.text(3.85, 4500, "r = required return rate %", fontsize=12, color="black")
plt.text(3.85, 3832, "Most Recent Dividend: Rs 64", fontsize=12, color="black")
plt.text(3.85, 3166, "Share Price: Rs 2,161.10", fontsize=12, color="black")
plt.text(3.85, 2500, "(13/06/26)", fontsize=10, color="black")
plt.text(5, 7000, "Equation:", fontsize=12, color="black")
plt.text(5, 6500, "P = D1/(r-g)", fontsize=12, color="black")
plt.legend()  

plt.show()