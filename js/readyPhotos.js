(function () {
    var container = document.querySelector(".container");
    reddit.top("aww").t("day").limit(10).fetch(function (res) {
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
        title.className = "tooltiptext";
        thumbnail.className = "thumbnail";
        thumbnail.setAttribute("src", awwData.thumbnail);

        link.setAttribute("href", "http://www.reddit.com" + awwData.permalink);
        link.setAttribute("target", "_blank");
        title.innerText = awwData.title;
        left.appendChild(link);
        link.appendChild(thumbnail);
        thumbnail.appendChild(title);

        row.appendChild(left);
        aww.className = "img-responsive";
        aww.setAttribute("src", awwData.url);
        container.appendChild(row);
      }
    });
  })();
