// javascript for stats class basic page

let replacement_check;
let replacement_bool;
let get_my_stats;
let results;
let go_back_data;
let sample_space_div;
let sample_space_form;
var count = 0;
/*  let users create the amount of samples needed instead of hard coding
let sample1desc;
let sample1num;
let sample2desc;
let sample2num;
let sample3desc;
let sample3num;
let sample4desc;
let sample4num;
*/
const max_sample_set_count = 10
var sample_set = []
let add_sample;
var sample_set_secondary = []

function set_DOM_elements() {
    replacement_check = document.getElementById("replacement");
    sample_space_div = document.getElementById("sample_space_div");
    //console.log("sample_space_div = ", sample_space_div)
    sample_space_form = document.getElementById("sample_space_form");
    get_my_stats = document.getElementById("get_my_stats");
    results = document.getElementById("results");
    go_back_data = document.getElementById("go_back_data");
    add_sample = document.getElementById("add_sample");
    //console.log("DOM ELEMENTS SET ....")
}

function assign_list(desc, num) {
    var ul = document.getElementById("list_results");
    var li = document.createElement("li");
    var valid = check_integer(num)
    if (valid) {
        add_line = "The " + desc + " probability is: P(x) = " + num.toString();
    }
    else {
        console.log(`valid = ${valid} else clause in assign_list active`)
        add_line = "This data field was not filled in."
    }
    li.appendChild(document.createTextNode(add_line));
    ul.appendChild(li);
}
function add_to_form(sample_dict) {
    // see create_sample_item for dict details
    //var input = document.createElement("input");
    //input.type = "text";
    //input.name = "member" + i;
    /*new_sample = {
            'description': description,
            'description_text': description_text,
            'sample_range': sample_range,
            'sample_range_text': sample_range_text,
            'item_id': item_id,
        }
    */

    //Create the div
    var new_div = document.createElement("div");
    new_div.id = sample_dict['item_id'];
    new_div.className = "flex_box_row";
    //create the label for text
    var new_label = document.createElement("label");
    new_label.for = sample_dict['description'];
    new_label.innerHTML = sample_dict['description_text']
    //create the input for text
    var new_input_desc = document.createElement("input");
    new_input_desc.type = "text";
    new_input_desc.name = sample_dict['description'];
    new_input_desc.id = sample_dict['description'];
    // the integer lable & input
    var new_label_num = document.createElement("label");
    new_label_num.for = sample_dict['sample_range'];
    new_label_num.innerHTML = sample_dict['sample_range_text'];

    var new_input_num = document.createElement("input");
    new_input_num.type = "number";
    new_input_num.name = sample_dict['sample_range'];
    new_input_num.id = sample_dict['sample_range'];

    //append to div
    new_div.appendChild(new_label)
    new_div.appendChild(new_input_desc)
    new_div.appendChild(new_label_num)
    new_div.appendChild(new_input_num)

    sample_space_form.appendChild(new_div)


}
function create_sample_item() {
    len = sample_set.length
    item_count = len + 1;
    if (item_count > max_sample_set_count) {
        alert("Can not add any more samples at this time.")
    }
    else {
        description = "sample" + item_count.toString() + "d";
        description_text = "sample " + item_count.toString() + " description: ";
        sample_range = "sample" + item_count.toString() + "n";
        sample_range_text = "sample " + item_count.toString() + " amount: ";
        item_id = "sample" + item_count.toString();
        new_sample = {
            'description': description,
            'description_text': description_text,
            'sample_range': sample_range,
            'sample_range_text': sample_range_text,
            'item_id': item_id,
        }

        sample_set.push(new_sample);
        add_to_form(new_sample);
        /* for testing
        for (index = 0; index < len; index++) {
            x = sample_set[index]
            console.log(sample_set[index])
        };
        */



    }
}
function get_total() {
    // alist should be passed in as sample_set
    var total = parseInt(0);

    for (i = 0; i < sample_set.length; i++) {
        var dict = sample_set[i]
        var num = dict['sample_range']
        var int = document.getElementById(num).value
        //console.log(`var int from get_total is _${int}_`)
        var valid = check_integer(int)
        console.log(`valid from get_total = ${valid}`)

        if (valid) {
            var new_int = parseInt(int)

            /*
            console.log(`int variable from get_total = ${int}`)
            int = parseInt(num)
            console.log(`int variable from get_total = ${int}`)
            */
            total = total + new_int
        }
    }
    //console.log(`returned from get_total = ${total}`)
    return total
}

function get_prob(trial, total) {
    var valid = check_integer(trial)
    console.log(`get_prob() valid = ${valid}  total = ${total}`)
    if (check_integer(trial) && total != 0) {
        var probability = parseInt(trial) / parseInt(total)
        var fixed_prob = probability.toFixed(4)
        // use function to assign append results to the <div> results <ul>
        // assign_list(desc, num)
        return fixed_prob

    }
    else {
        //if check_integer fails, return false
        console.log("false returned from get_prob()")
        return false
    }
}

function get_samples() {
    len = sample_set.length
    total = get_total(sample_set); //<---- HERE

    console.log(`from get_samples len=${len} , total=${total} `)

    if (total > 0) {
        for (i=0; i < len; i++) {
            var dict = sample_set[i];
            var value_input_id = dict['sample_range']
            //console.log(`value_input_id = ${value_input_id}`)
            var value_description_id = dict['description']
            var dom_value_input = document.getElementById(value_input_id).value;
            //console.log(`dom_value_input from get_samples() = ${dom_value_input}`)
            var dom_description_value = document.getElementById(value_description_id).value;
            var result = get_prob(dom_value_input, total);
            //console.log(`from get_samples, result = ${result}`)
            if (result == false) {
                description = "NaN results";
                num = "NaN results";

                assign_list(dom_description_value, result);
            }
            else {

                assign_list(dom_description_value, result);
            }
        }
    }
    show_results();

}



/*  HARD CODED
function get_samples() {
    sample1desc = document.getElementById("sample_1d").value
    sample1num = document.getElementById("sample_1n").value
    //
    sample2desc = document.getElementById("sample_2d").value
    sample2num = document.getElementById("sample_2n").value
    //
    sample3desc = document.getElementById("sample_3d").value
    sample3num = document.getElementById("sample_3n").value
    //
    sample4desc = document.getElementById("sample_4d").value
    sample4num = document.getElementById("sample_4n").value
    //
    console.log("Values:")
    console.log(sample1desc, sample2desc, sample3desc, sample4desc);
    console.log(sample1num, sample2num, sample3num, sample4num);
    total = calculate(sample1num, sample2num, sample3num, sample4num);
    if (sample1desc.length >= 1 && check_integer(sample1num)) {
        var probability = parseInt(sample1num) / total
        var fixed_prob = probability.toFixed(4)
        // use function to assign append results to the <div> results <ul>
        // assign_list(desc, num)
        assign_list(sample1desc, fixed_prob)

    }
    if (sample2desc.length >= 1 && check_integer(sample2num)) {
        var probability = parseInt(sample2num) / total
        var fixed_prob = probability.toFixed(4)

        // use function to assign append results to the <div> results <ul>
        // assign_list(desc, num)
        assign_list(sample2desc, fixed_prob)

    }

    if (sample3desc.length >= 1 && check_integer(sample3num)) {
        var probability = parseInt(sample3num) / total
        var fixed_prob = probability.toFixed(4)

        // use function to assign append results to the <div> results <ul>
        // assign_list(desc, num)
        assign_list(sample3desc, fixed_prob)
    }
    if (sample4desc.length >= 1 && check_integer(sample4num)) {
        var probability = parseInt(sample4num) / total
        var fixed_prob = probability.toFixed(4)

        // use function to assign append results to the <div> results <ul>
        // assign_list(desc, num)
        assign_list(sample4desc, fixed_prob)
    }
}
*/

function get_value() {
    let item = this.attributes["name"].value
    let bool = this.checked
    let check_label = document.getElementById("on_off")
    if (bool == true) {
        this.value = true;
        if (item == "is_replaced") {
            check_label.innerHTML = "&nbsp&nbsp&nbsp ON";
            replacement_bool = true;
        }

    }
    else {
        this.value = false;
        if (item == "is_replaced") {
            check_label.innerHTML = "&nbsp&nbsp&nbsp OFF";
            replacement_bool = false;
        }
    }
    let val = this.value
    console.log('element active: ', item)
    console.log("items val = ", val)
    console.log("items checked state = ", bool)
    console.log('replacement_bool = ', replacement_bool)

}

function alter_text_checkbox(element) {
    element.innerHTML = "&nbsp&nbsp&nbsp ON";
}

function show_results() {
    sample_space_div.style.display = 'none';
    results.style.display = 'flex';
    results.style.zIndex = 3;

}
function check_integer(value) {

    var x = parseInt(value)
    if (isNaN(x)) {
        return false;
    }
    else {
        return true;
    }



}




function go_back_to_data() {
    results.style.display = 'none';
    results.style.zIndex = 1;
    sample_space_div.style.display = 'flex';
    sample_space_div.style.zIndex = 3;



}

function Event_listeners() {
    replacement_check.addEventListener('click', get_value);
    get_my_stats.addEventListener('click', get_samples);
    add_sample.addEventListener('click', create_sample_item);
    go_back_data.addEventListener('click', go_back_to_data);


}

window.onload = function () {
    set_DOM_elements();
    Event_listeners();


}