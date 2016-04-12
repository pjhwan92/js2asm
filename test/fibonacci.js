function main () {
	var p1 = 1, p2 = 1;

	tmp = 0;

	i = 0;
	j = 0;
	do {
	//for (i = 0; i < 100000; i ++) {
		do {
		//for (j = 0; j < 100000; j ++) {
			p1 += p2;
			do {
			//while (p1 > 10) {
				p1 /= 10;
			} while (p1 > 10);
			p2 = tmp;
			do {
			//while (p2 > 10) {
				p2 /= 10;
			} while (p2 > 10);
			tmp = p1;
			j ++;
		} while (j < 100000);
		i ++;
	} while (i < 100000);

	return 0.0;
}
