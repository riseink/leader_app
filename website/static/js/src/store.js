import { createStore, combineReducers } from "redux"
import navigation from "./reducers/navigation"
import leadership from "./reducers/leadership"
import violator from "./reducers/violator"
import intro_videos from "./reducers/intro_videos"
import aspect_ratio from "./reducers/aspect_ratio"

const reducers = combineReducers({
	navigation,
	leadership,
	violator,
	intro_videos,
	aspect_ratio,
})

const store = createStore(reducers)

store.subscribe(() => {
	if (process.env.NODE_ENV === "development") {
		console.log(store.getState())
	}
})

export default store
