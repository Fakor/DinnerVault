function display_plans(parent_id, plans, dinners) {
    var i;
    parent = document.getElementById(parent_id);
    for(i=0; i < 7; ++i){
        date = new Date();
        date.setDate(date.getDate()+i);
        create_empty_plan(parent, date);
        element_new_row(parent);
        element_new_row(parent);
    }
}

function create_empty_plan(parent, date){
    date_label = document.createElement("label");
    date_label.setAttribute("class", "plan")
    date_label.innerHTML = date_string(date);
    parent.appendChild(date_label);
}