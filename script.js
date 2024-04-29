function elimina(e) {
    var img_eliminar = precario.getElementsByTagName("img");
    var zIndexValue = 1000; 
    var index = 0;
    while (index < img_eliminar.length) {
        if (img_eliminar[index]) { 
            img_eliminar[index].style.position = "relative"; 
            img_eliminar[index].style.zIndex = zIndexValue;
            zIndexValue--;
            img_eliminar[index].parentNode.removeChild(img_eliminar[index]);
        }
    }
}

function mangiabilita(e){
    test=false;
    img= precario.getElementsByTagName("img");
    if (img[0].src.endsWith("culoSu.png") && img[img.length - 1].src.endsWith("culoGiu.png")){
        test=true;
    }
    console.log(test,"test")
    return test;
    
}

function errore(n){
    console.log(n,"\n");
}

function eliminaDiv(id){
    divDaEliminare = document.getElementById(id);
    divDaEliminare.parentNode.removeChild(divDaEliminare);
}

function attenzione(e){
    Swal.fire({
        icon: "warning",
        title: "Fai attenzione!"
    });
}
function declassato(e){
    Swal.fire({
        icon: "error",
        title: "Oh no!",
        text: "hai sbagliato il panino preferito del professore scibetta!\nTi ha fatto tornare indietro!"
        });
}
function vinto(e){
    Swal.fire({
        title: "Hai vinto!",
        text: "Grazie per avere giocato!",
        imageUrl: "https://i.gifer.com/4rv8.gif",
        imageWidth: 400,
        imageHeight: 300,
        imageAlt: "burger king"
      });
}

function riavvia(e){
    location.reload(); 
};

function lvl_superato(e){
    Swal.fire({
        position: "top-end",
        icon: "success",
        showConfirmButton: false,
        timer: 1500
      });
}
function inizio(e){
    Swal.fire({
        title: "È arrivato il tuo primo cliente, servilo! \nBuon game!",
        showClass: {
          popup: `
            animate__animated
            animate__backInDown
          `
        },
        hideClass: {
          popup: `
            animate__animated
            animate__fadeOutDown
            animate__faster
          `
        }
      });
}

function info(){
    Swal.fire({
        title: "Come si gioca?",
        text: "Dovrai preparare dei panini seguendo le richieste dei clienti che appaiono sulla schermata. Ogni cliente ha una richiesta diversa e devi assemblare il panino corrispondente, mi raccomando la parte sopra e sotto del panino devono stare nel punto giusto. Il punteggio aumenta ogni volta che il panino viene preparato correttamente e consegnato al cliente.\nPer selezionare gli ingredienti del panino puoi cliccare sugli elementi disponibili e se li riclicchi li rimuovi.\nIl pulsante 'Elimina' rimuove tutti gli ingredienti.\nIl pulsante 'Consegna' controlla se il panino è stato preparato correttamente e lo consegna al cliente.\nRendi tutti i clienti felici e vincerai!",
        showClass: {
            popup: `
              animate__animated
              animate__zoomIn
              animate__faster
            `
        },
        hideClass: {
            popup: `
              animate__animated
              animate__zoomOutDown
              animate__faster
            `
        },
        icon: "question"
      });
}

function squeesound(){
    var audio = document.getElementById("squeese");
    audio.play();
}
function foodSound(){
    var audio = document.getElementById("placing");
    audio.play();  
}
function removeSound(){
    var audio = document.getElementById("remove");
    audio.play();  
}
document.addEventListener('DOMContentLoaded', function() {
    var audio = document.getElementById("backsound");
    audio.play();
  });