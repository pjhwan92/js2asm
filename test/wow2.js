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

	/*for (i = 0; i < 10; i ++) {
		b[1] /= i
	}*/

	i = 0;
	i = 1
	i = 2
	i = 3
	e = 100;
	while (i < 100000000) {
		if (e % 2 == 0)
			e *= i
		else
			e *= i+1
		e = (e + 3) % 100232
		i ++
	}

	f = d (10 + e, 20 + b[2])

	return (e * 4 + f * 0xFF)
}

main ();

//a (10, 20)
