function wow (a,b) {
	do {
		if (a % 2 == 0)
			a *= a
		else
			a /= 10
	}while (a < 1000);
	return a + 10 * b, 10
}

function wow2 (a) {
	do {
		if (a % 2 == 0)
			a *= a
	} while (a < 100);

	return a + 10
}

function main () {
	c = 2;
	a = c == 3? 1 : 2;
	
	c += wow (1, 3)
	c += wow2 (2)

	c = a * c

	return c
}
