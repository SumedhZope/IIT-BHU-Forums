const openTab = (e, id_name) => {
    tabContent = document.getElementsByClassName("tabcontent");

    for(i = 0;i<tabContent.length;i++){
        tabContent[i].style.display = "none"; 
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    document.getElementById(id_name).style.display = "block";
    e.currentTarget.className += " active";
}

document.getElementById("defaultOpen").click();