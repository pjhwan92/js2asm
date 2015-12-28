function main () {
	j = 1;
	k = 1;
	while (j < 100000000) {
		k *= j;
		while (k > 10) {
			k /= 10;
		}
		j ++;
	}
	
	return 0.0;
}
