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

    create_plan(parent, id, name, dinner_id, text, all_dinners);
}

function create_plan(parent, id, name, dinner_id, text, all_dinners) {
    // Name input
    name_input = document.createElement("input");
    name_input.setAttribute("type", "text");
    name_input.setAttribute("name", id + "_NAME");
    name_input.setAttribute("value", name);

    // Selector for dinner
    let dinner_pick = document.createElement("select");
    dinner_pick.setAttribute("name", id + "_DINNER");
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
    text_input = document.createElement("textarea");
    text_input.setAttribute("type", "text");
    text_input.setAttribute("cols", 100);
    text_input.setAttribute("rows", 2);
    text_input.setAttribute("maxlength", 200);
    text_input.setAttribute("name", id + "_TEXT");
    text_input.innerHTML=text

    // Add all elements to parent
    parent.appendChild(name_input);
    parent.appendChild(dinner_pick);
    parent.appendChild(text_input);
    element_new_row(parent);
}

function create_empty_plan(parent_id, dinners_json){
    // Parse inputs
    parent = document.getElementById(parent_id);
    var dinners = JSON.parse(dinners_json);

    create_plan(parent, "NEW", "", "", "", dinners);
}
