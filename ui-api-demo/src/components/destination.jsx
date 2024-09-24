import { Card, CardHeader, Divider } from "@nextui-org/react";
import DayForecast from "./dayForecast";

const Destination = ({destination}) => {


    return ( 
        <div
        className="w-full bg-foreground-50 rounded-lg"
        >
           
                <h1
                className="text-xl font-bold p-4"
                >{destination.display}</h1>
            
            <Divider
            className="my-4"
            />
            {destination.weather.length > 0 ? <DayForecast weather={destination.weather} /> : <h1>No weather data available</h1>}
        </div>
     );
}
 
export default Destination;