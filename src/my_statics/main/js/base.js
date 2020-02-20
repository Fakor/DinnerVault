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

function create_date_picker(form_id) {
    let date_pick = document.createElement("select");
    date_pick.setAttribute("form", form_id);
    date_pick.setAttribute("name", "date_pick");
    date_pick.setAttribute("class", "date");

    today = new Date();

    var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    add_option(date_pick, "Today (" + date_string(today) + ")",  date_string(today));
    var tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate()-1);
    add_option(date_pick, "Yesterday (" + date_string(tomorrow) + ")",  date_string(tomorrow));

    var i;
    for(i=2; i < 9; ++i){
        var d = new Date(); 
        d.setDate(d.getDate()-i);
        let day_s = days[d.getDay()];
        add_option(date_pick, day_s + " (" + date_string(d) + ")", date_string(d));
    }

    let submit = document.createElement("input");
    submit.setAttribute("type", "submit");
    submit.setAttribute("value", "Add date");
    submit.setAttribute("name", "submit_date");
    submit.setAttribute("form", form_id);

    document.body.append(date_pick);
    document.body.append(submit);
}

function add_option(selector, text, value){
    option = document.createElement("option");
    option.setAttribute("value", value);
    option.innerHTML = text;
    selector.append(option);
}

function date_string(date){
    return date.getFullYear() + "-" + date.getMonth() + "-" + date.getDate();
}


