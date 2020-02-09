function create_header(path) {
    let header=document.createElement("div")
    header.setAttribute("class", "header");
    header.setAttribute("id", "header");
    img = document.createElement("img");
    img.setAttribute("src", path);
    header.appendChild(img)
    header.innerHTML+= "<br>"
    document.body.appendChild(header);
}

function add_header_button(text, path){
    let button=document.createElement("button");
    button.setAttribute("class", "top");
    button.onclick= function() {location.href=path;};
    button.setAttribute("type", "button");
    button.innerHTML = text;
    button.setAttribute("align" ,"right");
    header = document.getElementById("header");
    header.append(button);
}
