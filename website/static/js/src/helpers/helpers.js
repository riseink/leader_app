/*
*	@function onScroll
*
*	This function checks the position of the scrollbar and allows functions to be called
*	depending on the scroll position. 50ms Throttling is applied
*	
*	@position 		scroll positon when you want the callbacks to trigger
*	@trueCallback	this function will get called whe the scroll bar is greater than postion
*	@falseCallback	options function gets called if the scroll bar is less than position
*
*/
export function onScroll(position, trueCallback, falseCallback = function(){}) {
	$(window).scroll(throttle((e) =>
		($(window).scrollTop() >= position) ? trueCallback.call() : falseCallback.call()
	, 50)) // Change throttling value if triggers aren't frequent enought or performance is affected
}

export function onTransitionEnd(selector, callback) {
	$(selector).bind("transitionend webkitTransitionEnd oTransitionEnd MSTransitionEnd", callback());
}


function throttle (callback, limit) {
    var wait = false;
    return function () {               
        if (!wait) {                   
            callback.call();           
            wait = true;               
            setTimeout(function () {   
                wait = false;          
            }, limit);
        }
    }
}

/**
 * Force vimeo players to resize when a modal is opened.
 * Fixes a bug where modals w/ Vimeo players in them open
 * to an incorrect size. Copied from wagtail-vimeo/.../js/vimeo.js
 */
export const resizeVideosInModals = () => {
  // Get each video element on the page
  Array.from(document.querySelectorAll(".overlay .scc-video-component")).forEach(vimeoEl => {
    // Listen for clicks on that element
    vimeoEl.addEventListener('click', (e) => {
      let PROPER_RATIO = 0.5625
      let mediacopyVideo = $(e.currentTarget)
      let videoWrapper = $(e.currentTarget).find(".videoWrapper")
      if (videoWrapper.length <= 0) return

      let videoHeight = mediacopyVideo.height()
      let videoWidth = videoWrapper.width()
      let mediacopyWidth = mediacopyVideo.width()

      //videoWidth should be set to whichever width is smaller: the videoWrapper OR the containing mediacopy-video element
      videoWidth = mediacopyWidth < videoWidth ? mediacopyWidth : videoWidth

      let videoRatio = videoHeight / videoWidth
      let adjustedPadding = videoHeight - 40

      if (videoRatio <= PROPER_RATIO) {
        let adjustRatio = PROPER_RATIO - videoRatio
        let adjustFluidVideoWidth = videoWidth * (1 - adjustRatio)

        videoWrapper.css("width", adjustFluidVideoWidth)
        videoWrapper.css("paddingBottom", adjustedPadding)
      } else {
        videoWrapper.removeAttr("style")
      }
    })
  })
}


export const browserIsIE = () => !!window.MSInputMethodContext && !!document.documentMode
export const browserIsEdge = () => window.navigator.userAgent.indexOf("Edge/") > -1