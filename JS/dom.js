function abrirVentana(){
    let ventana = open("","nombre", "toolbar=no,menubar=no,status=yes,width=200,height=200,resizable=yes");
}


function confirmar(){
    if(confirm("Esta seguro que desea realizar el calculo?","Mensaje de Confirmacion")){
        alert('se ejecuto el calculo')
    }else{
        alert('Se Cancelo la operacion!')
    }
}

function esperarServidor(){
    setTimeout("tiempo()",5000)
}

function tiempo(){
    alert("se han recibido los datos del Servidor")
}

function esperarServidor2(){
    setTimeout(function(){
        alert("se han recibido los datos del Servidor, \nse han recibido los datos del Servidor")
    },2000)
}

function ejecutarEventoLibre(){
    document.addEventListener("click",function(){
         document.getElementById("demo").innerHTML ="Hello World!"
    })
}

function entrar(){
    document.getElementById("txt1").style.backgroundColor="#568923"
}
function salir(){
    document.getElementById("txt1").style.backgroundColor="#0f5"

}

function escribir(){
    document.getElementById("demo").innerHTML="Me estan escribiendo.."
}

let texto1 
let lineaTexto = 1
function addNode1(){
   // Instancia de objeto
    let texto1 = document.getElementById("txt1")
    let nt =document.createTextNode(texto1 + " " + lineaTexto + " - ")
    let nparrafo = document.getElementById("parrafo")
    nparrafo.appendChild(nt)
    lineaTexto= lineaTexto+1
}

function eliminarNode(){
    let nparrafo= document.getElementById("parrafo")
    if(nparrafo.hasChildNodes()){
        nparrafo.removeChild(nparrafo.lastChild)
    } else{
       alert('Ya no hay lineas para eliminar')
    }
}