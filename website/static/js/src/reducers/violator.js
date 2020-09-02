const initialState = { violatorVisible: true }

const violator = (state = initialState, action) => {
	switch(action.type) {
		case 'TOGGLE_VIOLATOR':
			return {
				...state,
				violatorVisible: !state.violatorVisible
			}
		default:
			return state
	}
}

export default violator