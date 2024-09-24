import { Card, CardBody, CardHeader, Divider } from "@nextui-org/react";
import { Cloud, Droplets, Thermometer, Wind } from "lucide-react";

const DayForecast = ({ weather }) => {
  function formatDate(dateString) {
    const date = new Date(dateString);
    const options = { year: "numeric", month: "long", day: "numeric" };
    const formattedDate = new Intl.DateTimeFormat("en-US", options).format(
      date
    );
    const weekday = new Intl.DateTimeFormat("en-US", {
      weekday: "long",
    }).format(date);

    return {
      weekday,
      formattedDate,
    };
  }

  const getWeatherIcon = (icon) => {
    const iconMap = {
      "01d": "☀️",
      "01n": "🌙",
      "02d": "⛅",
      "02n": "☁️",
      "03d": "☁️",
      "03n": "☁️",
      "04d": "☁️",
      "04n": "☁️",
      "09d": "🌧️",
      "09n": "🌧️",
      "10d": "🌦️",
      "10n": "🌧️",
      "11d": "⛈️",
      "11n": "⛈️",
      "13d": "❄️",
      "13n": "❄️",
      "50d": "🌫️",
      "50n": "🌫️",
    };
    return iconMap[icon] || "🌡️";
  };

  return (
    <div className="flex gap-2 flex-col max-w-full overflow-x-auto p-2 md:flex-row ">
      {weather.map((day, index) => (
        <Card className="grow min-w-[100%]  md:max-w-[350px] md:min-w-[250px]" key={index}>
          <CardHeader className="flex  flex-col items-start justify-start">
            <h4 className="text-md font-bold">
              {formatDate(day.date).formattedDate}
            </h4>
            <p className="text-sm text-foreground-500">
              {formatDate(day.date).weekday}
            </p>
          </CardHeader>
          <Divider className="mb-2" />
          <CardBody>
            <div className="flex relative flex-col items-center mb-6">
              <span
                className="text-sm text-foreground-500"
                className="text-6xl mb-2"
              >
                {getWeatherIcon(day.weather_icon)}
              </span>
              <h2 className="text-4xl font-bold">{day.temp.toFixed(1)}°C</h2>
              <p className="text-xl text-muted-foreground capitalize">
                {day.weather_description}
              </p>
            </div>
            <div className="grid grid-cols-2 gap-4">
              <div className="flex items-center">
                <Thermometer className="w-10 h-10 mr-2 text-blue-500" />
                <span className="text-sm text-foreground-500">
                  Feels like: {day.feels_like.toFixed(1)}°C
                </span>
              </div>
              <div className="flex items-center">
                <Droplets className="w-10 h-10 mr-2 text-blue-500" />
                <span className="text-sm text-foreground-500">
                  Humidity: {day.humidity}%
                </span>
              </div>
              <div className="flex items-center">
                <Wind className="w-10 h-10 mr-2 text-blue-500" />
                <span className="text-sm text-foreground-500">
                  Wind: {day.wind.speed.toFixed(1)} m/s
                </span>
              </div>
              <div className="flex items-center">
                <Cloud className="w-10 h-10 mr-2 text-blue-500" />
                <p className="text-sm text-foreground-500">
                  Clouds: {day.clouds.all}%
                </p>
              </div>
            </div>
            <div className="mt-6 text-sm text-muted-foreground">
              <p className="absolute text-center top-0 text-foreground-500 right-[5%] text-right flex flex-col">
                {day.temp_max.toFixed(1)}°C{" "}
                <span className="font-bold text-sm">Max</span>{" "}
              </p>
              <p className="absolute text-center text-foreground-500 top-0 left-[5%] text-left flex flex-col">
                {day.temp_min.toFixed(1)}°C
                <span className="font-bold">Min</span>{" "}
              </p>
              <p>
                <span className="font-bold">Pressure:</span> {day.pressure} hPa
              </p>
            </div>
          </CardBody>
        </Card>
      ))}
    </div>
  );
};

export default DayForecast;
