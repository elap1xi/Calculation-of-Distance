#include <stdio.h>
#include <math.h>
int main(int argc, char* argv[], char* env[]){
    int sc_d0, sc_p0, sc_d00, sc_p00;
	printf("Enter the longitude and latitude of the first location (Format : ddd.mmmmmm/dd.mmmmmm) : ");
	scanf("%d.%d/%d.%d", &sc_d0, &sc_p0, &sc_d00, &sc_p00);
	int se_d0, se_p0, se_d00, se_p00;
	printf("Enter the longitude and latitude of the second location (Format : ddd.mmmmmm/dd.mmmmmm) : ");
	scanf("%d.%d/%d.%d", &se_d0, &se_p0, &se_d00, &se_p00);
	float sc_m0, sc_l0, sc_s0, sc_l00, sc_m00, sc_s00;
	sc_l0 = (float)sc_p0 * 1 / 1000000 * 60;
	sc_m0 = (int)((float)sc_p0 * 1 / 1000000 * 60);
	sc_s0 = (((float)sc_l0 - (float)sc_m0) * 60);
	sc_l00 = (float)sc_p00 * 1 / 1000000 * 60;
	sc_m00 = (int)((float)sc_p00 * 1 / 1000000 * 60);
	sc_s00 = (((float)sc_l00 - (float)sc_m00) * 60);
	// printf("%f, %f, %f / %f, %f, %f", sc_d0, sc_m0, sc_s0, sc_d00, sc_m00, sc_s00);
	float se_m0, se_l0, se_s0, se_l00, se_m00, se_s00;
	se_l0 = (float)se_p0 * 1 / 1000000 * 60;
	se_m0 = (int)((float)se_p0 * 1 / 1000000 * 60);
	se_s0 = (((float)se_l0 - (float)se_m0) * 60);
	se_l00 = (float)se_p00 * 1 / 1000000 * 60;
	se_m00 = (int)((float)se_p00 * 1 / 1000000 * 60);
	se_s00 = (((float)se_l00 - (float)se_m00) * 60);
	// printf("\n%f, %f, %f / %f, %f, %f", se_d0, se_m0, se_s0, se_d00, se_m00, se_s00);
	float ca_d0, ca_m0, ca_s0, ca_d00, ca_m00, ca_s00;
	float r = 6378.135, d = 111.31945588668853276112184419674;
	double ck = cos((sc_d00 - se_d00) / 2) * d;
	ca_d0 = sc_d0 - se_d0;
	ca_m0 = sc_m0 - se_m0;
	ca_s0 = sc_s0 - se_s0;
	ca_d00 = sc_d00 - se_d00;
	ca_m00 = sc_m00 - se_m00;
	ca_s00 = sc_s00 - se_s00;
	// printf("\n\n%f, %f, %f, %f, %f, %f", ca_d0, ca_m0, ca_s0, ca_d00, ca_m00, ca_s00);
	float calc_1 = ca_d0 * ck;
	float calc_2 = ca_m0 * (ck / 60);
	float calc_3 = ca_s0 * (ck / 3600);
	float cal_1 = pow((calc_1 + calc_2 + calc_3), 2);
	float calc_4 = ca_d00 * d;
	float calc_5 = ca_m00 * (d / 60);
	float calc_6 = ca_s00 * (d / 3600);
	float cal_2 = pow((calc_4 + calc_5 + calc_6), 2);
	printf("Distance of two points : %.4fkm (%.4fm)",(cal_1+cal_2)*10,(cal_1+cal_2)*10000);
	return 0;
}
