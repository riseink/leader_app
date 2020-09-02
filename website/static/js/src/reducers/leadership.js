const initialState = { 
	people: [], 
	active_bio_id: 0
}

const leadership = (state = initialState, action) => {
	switch(action.type) {

		case 'GET_LEADERSHIP_SUCCESS':
			return {
				...state,
				people: action.people
			}
		case 'BIO_CLICK':
			return {
				...state,
				active_bio_id: action.id
			}
		default:
			return state;

	}
}

export default leadership