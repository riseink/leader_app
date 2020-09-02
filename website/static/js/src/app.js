// NPM imports
import "fetch-polyfill"
import "babel-polyfill"
import "object-fit-videos"

// Local styles
import styles from "../../css/src/app.scss"

// Local JS
import Menu from "./components/menu"
import MenuIcon from "./components/menu_icon"
import Violator from "./components/violator"
import IntroVideos from "./components/intro_videos"
import ScrollIndicator from "./components/ScrollIndicator.js"
import { muteVideosOnClose, removeInlineStyleIE } from "./components/videos"

import ScrollAnimations from "./helpers/ScrollAnimations.js"
import LazyLoad from "./helpers/LazyLoad"
import AspectRatio from "./helpers/AspectRatio"
import { resizeVideosInModals } from "./helpers/helpers"

// Wagtail Foundation styles
import styles_vimeo from "../../../../src/wagtail-vimeo/vimeo/static/css/src/vimeo.scss"
import styles_contact from "../../../../src/wagtail-contact/contact/static/css/src/contact.scss"
import styles_iframe from "../../../../src/wagtail-iframe/iframe/static/css/src/iframe.scss"

// Wagtail Foundation JS
import TabFilterJS from "../../../../src/wagtail-tabfilter/tabfilter/static/js/src/tabfilter.js"
import VimeoJS from "../../../../src/wagtail-vimeo/vimeo/static/js/vimeo.js"
import ExpandingVideoJS from "../../../../src/wagtail-vimeo/vimeo/static/js/expanding_video.js"

// Initialize components on document ready
$(document).ready(function() {
	// FORMAT Javascript_Class.init();
	AspectRatio.init()

	Menu.init()
	MenuIcon.init()

	Violator.init()

	TabFilterJS.init()

	VimeoJS.init()
	resizeVideosInModals()

	ExpandingVideoJS.init()
	ScrollAnimations.init()
	IntroVideos.init()
	LazyLoad.init()
	ScrollIndicator.init()

	muteVideosOnClose()
	removeInlineStyleIE()

	// Throttle the resize method
	let resizeId = null
	$(window).resize(() => {
		clearTimeout(resizeId)
		resizeId = setTimeout(initResizeComponents, 500)
	})
})

// Resize initializers
let initResizeComponents = function() {
	AspectRatio.init()
}
