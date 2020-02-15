function create_header(path, title) {
    let header=document.createElement("div")
    header.setAttribute("class", "header");
    header.setAttribute("id", "header");
    img = document.createElement("img");
    img.setAttribute("src", path);

    let l_div=document.createElement("div");
    l_div.setAttribute("align", "left");
    l_div.setAttribute("id", "head_l");

    let r_div=document.createElement("div");
    r_div.setAttribute("align", "right");
    r_div.setAttribute("id", "head_r");

    header.appendChild(r_div);
    header.appendChild(img);
    header.appendChild(l_div);


    document.body.appendChild(header);

    add_header_button("Overview", "/main/overview");
    add_header_button("Create dinner", "/main/create");
    add_header_button("Create label", "/main/create_label");

    let set_title=document.createElement("h2");
    set_title.innerHTML=title;
    l_div.append(set_title);

    add_header_button_right("Logout", "/logout");
}

function add_header_button(text, path){
    add_button_by_id(text, path, "head_l");
}

function add_header_button_right(text, path){
    add_button_by_id(text, path, "head_r");
}

function add_button_by_id(text, path, el_id) {
    let button=document.createElement("button");
    button.setAttribute("class", "top");
    button.onclick= function() {location.href=path;};
    button.setAttribute("type", "button");
    button.innerHTML = text;
    div = document.getElementById(el_id);
    div.append(button);
}
