const list_menu = [
    {
        "title": "Home",
        "value": "./index.html"
    },
    {
        "title": "About",
        "value": "./about.html"
    },
    {
        "title": "Tutorial",
        "value": ".#",
        "submenu": [
            {
                title: "Thủ thuật",
                value: "#"
            },
            {
                title: "Kiến Thức",
                value: "#"
            },
            {
                title: "Đồ họa",
                value: "#",
                submenu: [
                    {
                        title: "Audition",
                        value: "#"
                    },
                    {
                        title: "Illustrator",
                        value: "#"
                    },
                    {
                        title: "After Effect",
                        value: "#"
                    },
                    {
                        title: "Premiere",
                        value: "#"
                    }
                ]
            },
            {
                title: "Lập trình",
                value: "#"
            }
        ]
    },
    {
        "title": "Contact",
        "value": "./contact.html"
    },
    {
        "title": "Login",
        "value": "./login.html"
    }
];

const list = document.querySelector(".list-menu");
let count = 0;
const showNavbar = (listItems, partentItem) => {
    listItems.forEach(({ title, value, submenu = [] }) => {
        const el = document.createElement('li');
        const ahref = document.createElement('a');
        ahref.textContent = title;
        ahref.href = value;
        el.appendChild(ahref);

        if (submenu?.length) {
            const subList = document.createElement('ul');
            subList.className = "sub_list";
            el.className = 'special_sub_list';
            
            if(count) {
                el.classList = 'special_sub_list art'
            }

            el.appendChild(subList);
            
            count++;
            showNavbar(submenu, subList);
        }

        partentItem.appendChild(el);
    });

}

showNavbar(list_menu, list);
// handle style css