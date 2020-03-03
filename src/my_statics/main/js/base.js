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
    button.setAttribute("class", "top style1");
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
    date_pick.setAttribute("class", "date style1");

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
    submit.setAttribute("class", "style1");
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

function id_update_label_display(element, name, display) {
    element.oninput = function() {
        update_label_display(name, display);
    }
}

function update_label_display(name, display) {
    sl_r = document.getElementById(name + "_RED");
    sl_g = document.getElementById(name + "_GREEN");
    sl_b = document.getElementById(name + "_BLUE");
    text = document.getElementById(name + "_TEXT");
    display.innerHTML = text.value;

    style = "background-color: rgb(" + sl_r.value + "," + sl_g.value + "," + sl_b.value + ")"
    display.setAttribute("style", style);
}

function create_label_editor(name, parent_id) {
    p = document.getElementById(parent_id);
    row = document.createElement("div");
    row.setAttribute("class", "row");

    c1 = document.createElement("div");
    c1.setAttribute("class", "column2");
    c1.setAttribute("align", "center");

    c2 = document.createElement("div");
    c2.setAttribute("class", "column2");
    c2.setAttribute("align", "center");

    text = document.createElement("input");
    text.setAttribute("type", "text");
    text.setAttribute("name", name + "_TEXT");
    text.setAttribute("id", name + "_TEXT");

    red = create_color_slider(name, "red");
    green= create_color_slider(name, "green");
    blue = create_color_slider(name, "blue");

    display = document.createElement("label");
    display.setAttribute("class", "dinner_label");
    display.setAttribute("id", name + "_DISPLAY");

    submit = document.createElement("button");
    submit.setAttribute("type", "submit");
    submit.setAttribute("name", "create_label");
    submit.setAttribute("class", "style1");
    submit.setAttribute("value", "true");
    submit.innerHTML = "Create label";

    id_update_label_display(red, name, display);
    id_update_label_display(green, name, display);
    id_update_label_display(blue, name, display);
    id_update_label_display(text, name, display);

    c1.appendChild(text);
    element_new_row(c1);
    c1.appendChild(red);
    element_new_row(c1);
    c1.appendChild(green);
    element_new_row(c1);
    c1.appendChild(blue);
    element_new_row(c2);
    c2.appendChild(display);
    element_new_row(c2);
    element_new_row(c2);
    c2.appendChild(submit);
    row.appendChild(c1);
    row.appendChild(c2);
    p.appendChild(row);
}

function create_color_slider(name, color){
    slider = document.createElement("input");
    slider.setAttribute("type", "range");
    slider.setAttribute("id", name + "_" + color.toUpperCase());
    slider.setAttribute("name", name + "_" + color.toUpperCase());
    slider.setAttribute("class", "colorslider " + color);
    slider.setAttribute("min", 0);
    slider.setAttribute("max", 255);

    return slider;
}

function element_new_row(element) {
    element.appendChild(document.createElement("br"));
}


