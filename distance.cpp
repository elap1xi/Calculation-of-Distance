#include <stdio.h>
main(){
    float a1, a00, b0, b00;
    int sc_d0, sc_p0, sc_d00, sc_p00;
    printf("Enter the latitdue ~ ");
    scanf("%d.%d/%d.%d"&sc_d0,&sc_p0,&sc_d00,&sc_p00);
    int se_d0, se_p0, se_d00, se_p00;
    printf("Enter the second latitude ~ ");
    scanf("%d.%d/%d.%d"&se_d0,&se_p0,&se_d00,&se_p00);
    sc_p0 = sc_p0 * 1/1000000 * 60
    sc_p00 = sc_p00 * 1/1000000 * 60
    se_p0 = se_p0 * 1/1000000 * 60
    se_p00 = se_p00 * 1/1000000 * 60
}
