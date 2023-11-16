function Bresenham(Xo,Yo, X1, Y1){
    let Pk1,Xk1, Yk1;
    let DX = X1 - Xo;
    let DY = Y1 - Yo;
    let Pk = (2 * DY) - DX;
    const table = [];
    let steps = DX - 1;
    let n = 0;
    while (Xk1 !== X1 || Yk1 !== Y1){
        if(Pk < 0){
            Pk1 = Pk + (2 * DY);
            Xk1 = Xo + 1;
            Yk1 = Yo;
        }
        if(Pk >= 0){
            Pk1 = Pk + (2 * DY) - (2 * DX);
            Xk1 = Xo + 1;
            Yk1 = Yo + 1;
        }
        
        table.push({Pk, Pk1, Xk1, Yk1});
        Pk = Pk1;
        Xo = Xk1;
        Yo = Yk1;
        if(n === steps) break;
        n++;
    }
    console.log("the steps: ", steps);
    console.table(table);
}
//Bresenham(9,18,14,22);
//Bresenham(20, 10, 30, 18);
//Bresenham(100, 100, 200, 200);
//Bresenham(5, 6, 8, 9);