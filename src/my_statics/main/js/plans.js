function display_plans(parent_id, plans_json, dinners_json) {
    var i;
    var dinners = JSON.parse(dinners_json);
    var plans = JSON.parse(plans_json);
    parent = document.getElementById(parent_id);
    for(i = 0; i < plans.length; ++i) {
        display_plan(parent, plans[i], dinners);
    }
}

function display_plan(parent, plan, all_dinners) {
    name = plan["fields"]["name"]
    dinner_id = plan["fields"]["dinner"]
    text = plan["fields"]["text"]
    id = plan["pk"]

    create_plan(parent, id, "OLD", name, dinner_id, text, all_dinners);
}

function create_plan(parent, id, type, name, dinner_id, text, all_dinners) {
    // Name input
    name_input = document.createElement("input");
    name_input.setAttribute("type", "text");
    name_input.setAttribute("name", type + "_NAME");
    name_input.setAttribute("maxlength", 20);
    name_input.setAttribute("value", name);

    // Selector for dinner
    let dinner_pick = document.createElement("select");
    dinner_pick.setAttribute("name", type + "_DINNER");
    dinner_pick.setAttribute("value", "");
    no_pick = add_option(dinner_pick, "", "")
    var i;
    for(i=0; i < all_dinners.length; ++i){
        if(all_dinners[i]["pk"] == dinner_id){
            add_selected_option(dinner_pick, all_dinners[i]["fields"]["name"], all_dinners[i]["pk"])
        } else {
            add_option(dinner_pick, all_dinners[i]["fields"]["name"], all_dinners[i]["pk"])
        }
    }

    // Text input
    text_input = document.createElement("input");
    text_input.setAttribute("type", "text");
    text_input.setAttribute("maxlength", 30);
    text_input.setAttribute("name", type + "_TEXT");
    text_input.setAttribute("value", text);

    // Delete button
    delete_button = document.createElement("button");
    delete_button.setAttribute("class", "style1");
    delete_button.setAttribute("name", "delete_plan");
    delete_button.setAttribute("value", id);
    delete_button.innerHTML="DEL"

    // Id
    id_hidden = document.createElement("input");
    id_hidden.setAttribute("type", "hidden");
    id_hidden.setAttribute("name", type + "_ID");
    id_hidden.setAttribute("value", id);


    // Add all elements to parent
    parent.appendChild(name_input);
    parent.appendChild(dinner_pick);
    parent.appendChild(text_input);
    parent.appendChild(delete_button);
    parent.appendChild(id_hidden);
    element_new_row(parent);
    element_new_row(parent);
}

function create_empty_plan(parent_id, dinners_json){
    // Parse inputs
    parent = document.getElementById(parent_id);
    var dinners = JSON.parse(dinners_json);

    create_plan(parent, 0, "NEW", "", "", "", dinners);
}

function create_week_plan(parent_id, dinners_json, week_json) {
    week = JSON.parse(week_json);
    dinners = JSON.parse(dinners_json);
    parent = document.getElementById(parent_id);
    var i;
    for(i = 0; i < week.length; ++i){
        l = document.createElement("label");
        l.setAttribute("class", "plan");
        l.innerHTML=week[i]["day"];
        parent.appendChild(l);
        element_new_row(parent);
    }

}
