function d (i1, i2) {
	return i1 * i2
}

function main () {
	f = 0.0
	a = 2;
	var b = [3.0 + a +1, 4.1, 6.2, 8.4]
	c = 2.0
	if (b[0] == 2)
		b[1] = c * 2
	else if (c == 2) {
		c -= 2.0
	}

	for (i = 0; i < 10; i ++) {
		b[1] /= i
	}

	i = 0;
	i = 1
	i = 2
	i = 3
	while (i < 10) {
		b[3] += i
		i ++
	}

	f = d (10 + i, 20 + b[2])

	return (b[1] * 4 + c * 0xFF)
}

//a (10, 20)
