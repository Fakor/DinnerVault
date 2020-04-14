function display_plans(parent_id, plans_json, dinners_json) {
    var i;
    var dinners = JSON.parse(dinners_json);
    var plans = JSON.parse(plans_json);
    parent = document.getElementById(parent_id);

    for(i = 0; i < plans; ++i) {
        create_plan(plans[i]);
    }
}

function create_empty_plan(parent_id, dinners_json){
    // Parse inputs
    parent = document.getElementById(parent_id);
    var dinners = JSON.parse(dinners_json);

    // Name input
    name_input = document.createElement("input");
    name_input.setAttribute("type", "text");
    name_input.setAttribute("id", "new_plan_name");
    name_input.setAttribute("name", "NEW_NAME");
    name_input.setAttribute("value", "");

    // Selector for dinner
    let dinner_pick = document.createElement("select");
    dinner_pick.setAttribute("id", "new_plan_dinner");
    dinner_pick.setAttribute("name", "NEW_DINNER");
    dinner_pick.setAttribute("value", "");
    no_pick = add_option(dinner_pick, "", "")
    var i;
    for(i=0; i < dinners.length; ++i){
        add_option(dinner_pick, dinners[i]["fields"]["name"], dinners[i]["pk"])
    }

    // Text input
    text_input = document.createElement("textarea");
    text_input.setAttribute("type", "text");
    text_input.setAttribute("id", "new_plan_text");
    text_input.setAttribute("cols", 100);
    text_input.setAttribute("rows", 2);
    text_input.setAttribute("maxlength", 200);
    text_input.setAttribute("name", "NEW_TEXT");

    // Add all elements to parent
    parent.appendChild(name_input);
    parent.appendChild(dinner_pick);
    parent.appendChild(text_input);
    element_new_row(parent);
}
