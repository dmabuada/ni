(function(a) {
    a.fn.extend({
        productGallery: function(b) {
            var c = {
                mainImage: ".placeholder"
            };
            return b = a.extend(c, b), this.each(function() {
                var c = a(this).find("a"),
                    d = a(this).siblings().find(b.mainImage);
                c.on("click", function(b) {
                    b.preventDefault();
                    var c = a(this).attr("href");
                    d.attr("src", c);
                });
            });
        }
    });
})(jQuery);

jQuery(document).ready(function () {
  jQuery('.thumbnails').productGallery({
    mainImage: '.custom'
  });
});