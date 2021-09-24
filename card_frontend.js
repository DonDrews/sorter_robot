var session_head;

function fetch_cards()
{
    console.log("fetching!");
    setTimeout(function() {
        req = new XMLHttpRequest();
        req.onload = function() {
            let tab = document.getElementById("cardtable");
            let resp = JSON.parse(this.responseText);

            if(resp.was_reset)
            {
                //only safe because there are no memory leaks in POD
                //will need to be changed if we add more to these nodes
                tab.innerHTML = "";
            }

            resp.cards.forEach(function (item, index) {
                let row = document.createElement('tr');
                let name = document.createElement('td');
                let set = document.createElement('td');
                name.innerHTML = item.name;
                set.innerHTML = item.set;
                row.append(name, set);
                tab.append(row);
            });
            fetch_cards();
        }
        req.open("GET", "/json?index=0");
        req.send();
    }, 10000)
}