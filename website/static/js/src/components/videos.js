import { browserIsIE, browserIsEdge } from "../helpers/helpers"

/**
 *  Find all overlay modals and listen for their close events.
 *  If they contain videos (Vimeo or HTML5) ensure the video is muted/destroyed
 *  when the modal is closed.
 */
export const muteVideosOnClose = () => {
	$(".overlay-trigger").on("mfpBeforeClose", function() {
		// figure out if this modal uses HTML5 video player or vimeo player
		const modalContent = document.querySelector(".mfp-content")
		const vimeoComponent = modalContent.querySelector(".vimeocopy")
		const usesVimeoPlayer = !!vimeoComponent

		if (usesVimeoPlayer) {
			// delete vimeo player iframes on modal close,
			// otherwise it will start playing again while hidden
			deleteVimeoIframeOnClose(vimeoComponent)
		} else {
			// look for HTML5 video inside the modal
			const video = document.querySelector(".mfp-content video")
			// if found, pause it
			if (video) video.pause()
		}
	})
}

/**
 *  Remove the Vimeo player iFrame from the DOM to avoid it playing while hidden
 *
 *  Mimic what's happening in wagtail-vimeo/.../vimeo.js:
 *  - show looping video (includes the play button, which rebuilds the iframe on click)
 *  - clear embedded video's inner html (the iframe)
 */
export const deleteVimeoIframeOnClose = (vimeoComponent) => {
	if (!vimeoComponent) return
	let loopingVideo = $(vimeoComponent).find(".looping-video")
	let embeddedVideo = $(vimeoComponent).find(".embedded-video")
	loopingVideo.show()
	embeddedVideo.html("")
}

/**
 *  In IE and Edge browsers, fix an issue where the object-fit-videos poyfill sets the video element's
 *  height and width to 0px.
 */
export const removeInlineStyleIE = () => {
	// Overlay trigger elements themselves don't tell you anything about the content inside their overlay;
	// therefore we need to listen to all overlay triggers for "open" events, and once open, check the content inside
	const OVERLAY_TRIGGERS = ".overlay-trigger"

	const isMicrosoftBrowser = browserIsIE() || browserIsEdge()
	if (!isMicrosoftBrowser) return

	// On modal open...
	$(OVERLAY_TRIGGERS).on("mfpOpen", function() {
		// Check if there's an HTML5 video in the modal
		const modalContent = document.querySelector(".mfp-content")
		const modalVideo = modalContent.querySelector(".video-modal__video")
		if (!modalVideo) return

		// Remove inline height and width set by the object-fit polyfill
		modalVideo.style.width = null
		modalVideo.style.height = null
	})
}
