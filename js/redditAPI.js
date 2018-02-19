function userSelect(item) {
    console.log("hello API");

    if (item == undefined || item == '') {
          item = "cats";
    };

    console.log("Word:" + item);
    var container = document.querySelector(".container");
    reddit.top(item).t("day").limit(10).fetch(function (res) {
      for (var i = 0; i < res.data.children.length; i++) {
        var awwData = res.data.children[i].data;
        var thumbnail = document.createElement("img");
        var aww = document.createElement("img");
        var row = document.createElement("div");
        var left = document.createElement("div");
        var link = document.createElement("a");
        var title = document.createElement("span");

        row.className = "row";
        left.className = "col-xs-4";
        title.className = "tooltip";
        thumbnail.setAttribute("src", awwData.thumbnail);

        link.setAttribute("href", "http://www.reddit.com" + awwData.permalink);
        link.setAttribute("target", "_blank");
        title.innerText = awwData.title;
        aww.className = "img-responsive";
        aww.setAttribute("src", awwData.url);

        link.appendChild(thumbnail);
        left.appendChild(title);
        left.appendChild(link);
        row.appendChild(left);
        container.appendChild(row);
      }
    });
  };