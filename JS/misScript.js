   // Metodo de operacion
   function operacion() {
    var a = 5  /*Declara la bariable globalmente*/
    const b = 3 /*Declara la variable como una constante*/
    let c = a + b  /*Declara la variable de una manera Local cosa qeucundo termina su funcion esta variable se limpia y no ocupa espacio en memoria como en el caso de var*/
    alert("La suma de " + a + " con " + b + " es " + c)
  
    a = parseInt(prompt("Ingrese un valor","Escriba un nuemero..."))
    let d = parseInt(prompt("Ingrese otro valor","Escriba un nuemero..."))
    c = a * d
}

    function suma(a,b){
        let c = a + b
        return ("La suma de " + a + " con " + b + " es " + c)
    }

    function resta(a,b){
        let c = a - b
        document.write("<h3>La Resta de " + a + " con " + b + " es " + c + "<br></h3>")
    }

    function multiplicacion(a,b){
        let c = a * b
        document.write("<h3>La Multiplicacion de " + a + " con " + b + " es " + c + "<br></h3>")
    }


    function division(a,b){
        let c = a / b
        if(b == 0){
            alert("no se Puede dividir por 0")
        }else{
            document.write("<h3>La Division de " + a + " con " + b + " es " + c + "<br></h3>")
        }
    }

    function hola(){
        let messageText ="Hola mundo"
        return messageText
    }

    function accederParrafo(){
        document.getElementById('parrafo1').innerHTML="esta es una linea<br> esta es una segunda linea <br>"
    }

    function limpiarParrafo(){
        document.getElementById('parrafo1').innerHTML=""
    }

    function calcular(){
        let a = parseInt(document.getElementById('txt1').value)
        let d = parseInt(document.getElementById('txt2').value)
        suma(a,d)
     /*   resta(a,d)
        multiplicacion(a,d)
        division(a,d)*/
        document.getElementById('txt3').value=suma(a,d)
    }
