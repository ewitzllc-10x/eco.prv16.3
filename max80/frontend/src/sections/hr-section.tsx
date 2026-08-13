import CardLink3 from "../components/card-link3";
import { CardLink3_cids } from "../_cids";
import { CardLink3_styles } from "../_styles";
import { cardLink3Data as cardLink3DataContent } from "../content";
/** Hr section. */
export default function HrSection({ cardLink3Data = cardLink3DataContent } = {}) {
  return (
    <div className="flex flex-col gap-4" data-cid="n334">
      <div className="flex flex-col gap-1" data-cid="n335">
        <h2 className="block text-color-001 text-xl font-semibold leading-7" data-cid="n336" data-component="heading">
          HR
        </h2>
      </div>
      <div className="grid gap-4 grid-rows-2 grid-cols-3 max-md:grid-rows-6 max-md:grid-cols-1 md:max-lg:grid-rows-3 md:max-lg:grid-cols-2" data-cid="n337">
        {cardLink3Data.map((d, i) => <CardLink3 key={i} d={d} cids={CardLink3_cids[i]} styles={CardLink3_styles[i]} />)}
      </div>
    </div>
  );
}
