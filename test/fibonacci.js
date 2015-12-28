function main () {
	var p1 = 1, p2 = 1;

	tmp = 0;

	for (i = 0; i < 100000; i ++) {
		for (j = 0; j < 100000; j ++) {
			p1 += p2;
			while (p1 > 10) {
				p1 /= 10;
			}
			p2 = tmp;
			while (p2 > 10) {
				p2 /= 10;
			}
			tmp = p1;
		}
	}

	return 0.0;
}
