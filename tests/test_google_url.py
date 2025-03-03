from locations.google_url import url_to_coords


def test_embed():
    assert url_to_coords(
        "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2421.2988280554714!2d1.2830013158163067!3d52.636513979836515!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47d9e161f2318f3f%3A0x1011fac48e8edcbf!2sNorwich+Depot+-+Parcelforce+Worldwide!5e0!3m2!1sen!2sus!4v1496935482694"
    ) == (52.636513979836515, 1.2830013158163067)
    assert url_to_coords(
        "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2500.3404587315936!2d0.2883177157631218!3d51.1943779795849!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47df48b0a94080d3%3A0xa460c3bddd378d92!2sTonbridge+Depot+-+Parcelforce+Worldwide!5e0!3m2!1sen!2sus!4v1496934862229"
    ) == (51.1943779795849, 0.2883177157631218)


def test_staticmap():
    assert url_to_coords(
        "https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyADmrIiwwDonRBd0CtDv0ir5EpreGZINmA&center=57.1614,-2.1123&size=730x400&zoom=15&markers=icon:https://www.puregym.com/images/map-selected.png%7Clabel:S%7C57.1614,-2.1123&style=feature:all%7Celement:labels.text.fill%7Csaturation:36&style=feature:all%7Celement:labels.text.fill%7Ccolor:0x333333&style=feature:all%7Celement:labels.text.fill%7Clightness:40&style=feature:all%7Celement:labels.text.stroke%7Cvisibility:on&style=feature:all%7Celement:labels.text.stroke%7Ccolor:0xffffff&style=feature:all%7Celement:labels.text.stroke%7Clightness:16&style=feature:all%7Celement:labels.icon%7Cvisibility:off&style=feature:administrative%7Celement:geometry.fill%7Ccolor:0xfefefe&style=feature:administrative%7Celement:geometry.fill%7Clightness:20&style=feature:administrative%7Celement:geometry.stroke%7Ccolor:0xfefefe&style=feature:administrative%7Celement:geometry.stroke%7Clightness:17&style=feature:administrative%7Celement:geometry.stroke%7Cweight:1.2&style=feature:landscape%7Celement:geometry%7Ccolor:0xe1e1e1&style=feature:landscape%7Celement:geometry%7Clightness:20&style=feature:poi%7Celement:geometry%7Ccolor:0xd2d2d2&style=feature:poi%7Celement:geometry%7Clightness:21&style=feature:poi.park%7Celement:geometry%7Ccolor:0xd2d2d2&style=feature:poi.park%7Celement:geometry%7Clightness:21&style=feature:road.highway%7Celement:geometry.fill%7Ccolor:0xffffff&style=feature:road.highway%7Celement:geometry.fill%7Clightness:17&style=feature:road.highway%7Celement:geometry.stroke%7Ccolor:0xffffff&style=feature:road.highway%7Celement:geometry.stroke%7Clightness:29&style=feature:road.highway%7Celement:geometry.stroke%7Cweight:0.2&style=feature:road.arterial%7Celement:geometry%7Ccolor:0xffffff&style=feature:road.arterial%7Celement:geometry%7Clightness:18&style=feature:road.local%7Celement:geometry%7Ccolor:0xffffff&style=feature:road.local%7Celement:geometry%7Clightness:16&style=feature:transit%7Celement:geometry%7Ccolor:0xf2f2f2&style=feature:transit%7Celement:geometry%7Clightness:19&style=feature:water%7Celement:geometry%7Ccolor:0xe9e9e9&style=feature:water%7Celement:geometry%7Clightness:17&style=feature:water%7Celement:geometry.fill%7Ccolor:0xc7e3e6&style=feature:water%7Celement:geometry.fill%7Cgamma:1.00"
    ) == (57.1614, -2.1123)
    assert url_to_coords(
        "https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyADmrIiwwDonRBd0CtDv0ir5EpreGZINmA&center=50.7208,-1.8841&size=730x400&zoom=15&markers=icon:https://www.puregym.com/images/map-selected.png%7Clabel:S%7C50.7208,-1.8841&style=feature:all%7Celement:labels.text.fill%7Csaturation:36&style=feature:all%7Celement:labels.text.fill%7Ccolor:0x333333&style=feature:all%7Celement:labels.text.fill%7Clightness:40&style=feature:all%7Celement:labels.text.stroke%7Cvisibility:on&style=feature:all%7Celement:labels.text.stroke%7Ccolor:0xffffff&style=feature:all%7Celement:labels.text.stroke%7Clightness:16&style=feature:all%7Celement:labels.icon%7Cvisibility:off&style=feature:administrative%7Celement:geometry.fill%7Ccolor:0xfefefe&style=feature:administrative%7Celement:geometry.fill%7Clightness:20&style=feature:administrative%7Celement:geometry.stroke%7Ccolor:0xfefefe&style=feature:administrative%7Celement:geometry.stroke%7Clightness:17&style=feature:administrative%7Celement:geometry.stroke%7Cweight:1.2&style=feature:landscape%7Celement:geometry%7Ccolor:0xe1e1e1&style=feature:landscape%7Celement:geometry%7Clightness:20&style=feature:poi%7Celement:geometry%7Ccolor:0xd2d2d2&style=feature:poi%7Celement:geometry%7Clightness:21&style=feature:poi.park%7Celement:geometry%7Ccolor:0xd2d2d2&style=feature:poi.park%7Celement:geometry%7Clightness:21&style=feature:road.highway%7Celement:geometry.fill%7Ccolor:0xffffff&style=feature:road.highway%7Celement:geometry.fill%7Clightness:17&style=feature:road.highway%7Celement:geometry.stroke%7Ccolor:0xffffff&style=feature:road.highway%7Celement:geometry.stroke%7Clightness:29&style=feature:road.highway%7Celement:geometry.stroke%7Cweight:0.2&style=feature:road.arterial%7Celement:geometry%7Ccolor:0xffffff&style=feature:road.arterial%7Celement:geometry%7Clightness:18&style=feature:road.local%7Celement:geometry%7Ccolor:0xffffff&style=feature:road.local%7Celement:geometry%7Clightness:16&style=feature:transit%7Celement:geometry%7Ccolor:0xf2f2f2&style=feature:transit%7Celement:geometry%7Clightness:19&style=feature:water%7Celement:geometry%7Ccolor:0xe9e9e9&style=feature:water%7Celement:geometry%7Clightness:17&style=feature:water%7Celement:geometry.fill%7Ccolor:0xc7e3e6&style=feature:water%7Celement:geometry.fill%7Cgamma:1.00"
    ) == (50.7208, -1.8841)
    assert url_to_coords(
        "https://maps.googleapis.com/maps/api/staticmap?center=50.7208,-1.8841&size=730x400&zoom=15&markers=icon:https://www.puregym.com/images/map-selected.png%7Clabel:S%7C50.7208,-1.8841&style=feature:all%7Celement:labels.text.fill%7Csaturation:36&style=feature:all%7Celement:labels.text.fill%7Ccolor:0x333333&style=feature:all%7Celement:labels.text.fill%7Clightness:40&style=feature:all%7Celement:labels.text.stroke%7Cvisibility:on&style=feature:all%7Celement:labels.text.stroke%7Ccolor:0xffffff&style=feature:all%7Celement:labels.text.stroke%7Clightness:16&style=feature:all%7Celement:labels.icon%7Cvisibility:off&style=feature:administrative%7Celement:geometry.fill%7Ccolor:0xfefefe&style=feature:administrative%7Celement:geometry.fill%7Clightness:20&style=feature:administrative%7Celement:geometry.stroke%7Ccolor:0xfefefe&style=feature:administrative%7Celement:geometry.stroke%7Clightness:17&style=feature:administrative%7Celement:geometry.stroke%7Cweight:1.2&style=feature:landscape%7Celement:geometry%7Ccolor:0xe1e1e1&style=feature:landscape%7Celement:geometry%7Clightness:20&style=feature:poi%7Celement:geometry%7Ccolor:0xd2d2d2&style=feature:poi%7Celement:geometry%7Clightness:21&style=feature:poi.park%7Celement:geometry%7Ccolor:0xd2d2d2&style=feature:poi.park%7Celement:geometry%7Clightness:21&style=feature:road.highway%7Celement:geometry.fill%7Ccolor:0xffffff&style=feature:road.highway%7Celement:geometry.fill%7Clightness:17&style=feature:road.highway%7Celement:geometry.stroke%7Ccolor:0xffffff&style=feature:road.highway%7Celement:geometry.stroke%7Clightness:29&style=feature:road.highway%7Celement:geometry.stroke%7Cweight:0.2&style=feature:road.arterial%7Celement:geometry%7Ccolor:0xffffff&style=feature:road.arterial%7Celement:geometry%7Clightness:18&style=feature:road.local%7Celement:geometry%7Ccolor:0xffffff&style=feature:road.local%7Celement:geometry%7Clightness:16&style=feature:transit%7Celement:geometry%7Ccolor:0xf2f2f2&style=feature:transit%7Celement:geometry%7Clightness:19&style=feature:water%7Celement:geometry%7Ccolor:0xe9e9e9&style=feature:water%7Celement:geometry%7Clightness:17&style=feature:water%7Celement:geometry.fill%7Ccolor:0xc7e3e6&style=feature:water%7Celement:geometry.fill%7Cgamma:1.00"
    ) == (50.7208, -1.8841)


def test_maps_url():
    assert url_to_coords("https://www.google.com/maps/@52.578594,-2.112396,15z") == (
        52.578594,
        -2.112396,
    )
    assert url_to_coords(
        "http://maps.google.com/maps?saddr=current+location&ll=57.213,-2.187"
    ) == (
        57.213,
        -2.187,
    )


def test_directions():
    assert url_to_coords(
        "https://www.google.com/maps/dir//51.4063062, -0.02920658/"
    ) == (
        51.4063062,
        -0.02920658,
    )
