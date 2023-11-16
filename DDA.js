function DDA(Xo, Yo, Xn, Yn) {
    const table = [];
    // Declare Variables
    let Xp, Yp, Xp1, Yp1, Xp1r, Yp1r;
    // Calculate Slope
    let DX = Xn - Xo;
    let DY = Yn - Yo;
    let M = DY / DX;
    Xp = Xo;
    Yp = Yo;
    // Calculate the number of Steps
    let Steps = 0;
    if(Math.abs(DX) > Math.abs(DY)){
        Steps = DX;
    }
    else {
        Steps = DY;
    }
    let n = 0;
    // Calculate the new points
    while (Xp1 !== Xn && Yp1 !== Yn){   
         if (M < 1){
            Xp1 = 1 + Xp;
            Yp1 = M + Yp;
        }
        if(M > 1){
            Xp1 = (1 / M) + Xp;
            Yp1 = 1 + Yp;
        }
        if ( M === 1) {
            Xp1 =  1 + Xp;
            Yp1 = 1 + Yp;
        }
        Xp1r = Math.round(Xp1);
        Yp1r  = Math.round(Yp1)     
         table.push({Xp, Yp, Xp1, Yp1, Xp1r, Yp1r});
         Xp = Xp1;
         Yp = Yp1;
         n+=1;
        if(n === Steps) break;
        
    }
    console.log("the steps ", Steps);
    // Print table
    console.table(table);
};
// DDA(5,6,8,12);
//DDA(1,7,11,17 )
DDA(100,200,500,300);