import store from '../store';

var MenuIcon = {
    els: null,
    elOpen: null,
    elClose: null,

    init() {
        this.els = document.getElementsByClassName('nav-menu-icon');
        this.elOpen = document.getElementById("menu_icon");
        this.elClose = document.getElementById("close_icon");
        this.initStateListener();
        this.initClickListener();
        this.render(store.getState().navigation)
    },

    initStateListener() {
        store.subscribe(() =>
            this.render(store.getState().navigation)
        )
    },

    initClickListener() {
        Array.from(this.els).forEach(function (element) {
            element.addEventListener("click", (e) => {
                e.preventDefault();
                store.dispatch({type: "TOGGLE_MENU"});
            })
        });
    },

    renderIcon(filename) {
        $(this.elOpen).find('i').text(filename);
    },

    render(state) {
        var filename = (state.menuVisible) ? "clear" : "menu";
        this.renderIcon(filename)
    }
};

export default MenuIcon;