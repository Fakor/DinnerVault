function create_dinner_button(dinner_name, dinner_id, dinner_info_id) {
    // Get info for dinner from dinner_info_id
    info = document.getElementById(dinner_info_id).innerHTML;

    // Get parent element from dinner_id
    parent = document.getElementById(dinner_id + "_button");

    // Create buttons that redirects you to the details for the dinner
    button = document.createElement("button");
    button.setAttribute("type", "submit");
    button.setAttribute("formmethod", "get");
    if(info) {
        button.setAttribute("class", "dinner_info");
    } else {
        button.setAttribute("class", "dinner");
    }
    button.setAttribute("name", "meal_details");
    button.onclick = function() {location.href="/main/detail/" + dinner_id + "/"}
    button.innerHTML = dinner_name;

    // Add elements to parents
    parent.appendChild(button);

}