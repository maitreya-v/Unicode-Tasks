const options = {
  method: 'GET',
  url: 'https://corona-virus-world-and-india-data.p.rapidapi.com/api',
  headers: {
    'X-RapidAPI-Key': 'c3036fcdfbmsh3e972fddd6f763cp14889djsn128248ee22ea',
    'X-RapidAPI-Host': 'corona-virus-world-and-india-data.p.rapidapi.com'
  }
};

axios.request(options)
.then(function (response) {
	console.log(response.data.countries_stat);
    //initializing
    let tabledata="";
    //problem faced:-was doing response.map but it is not iterable
    //mapping values
    response.data.countries_stat.map((values)=>{
        // if i wrote tabledata=`<tr>...`  it will only display the last value and not all the values
        tabledata+=`<tr>
        <td>${values.country_name}</td>
        <td>${values.cases}</td>
        <td>${values.deaths}</td>
        <td>${values.total_recovered}</td>
    </tr>`;
    });
    //changing the HTML of the target id with tabledata
    document.getElementById("table_body").innerHTML=tabledata;
})
