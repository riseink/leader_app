const initialState = { menuVisible: false }

const navigation = (state = initialState, action) => {
	switch(action.type) {
	case 'TOGGLE_MENU':
		return {
			...state,
			menuVisible: !state.menuVisible
		}
	default:
		return state
	}
}

export default navigation