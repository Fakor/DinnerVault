function create_header(path) {
    let header=document.createElement("div")
    header.setAttribute("class", "header");
    img = document.createElement("img");
    img.setAttribute("src", path);
    header.appendChild(img)
    document.body.appendChild(header);
}
