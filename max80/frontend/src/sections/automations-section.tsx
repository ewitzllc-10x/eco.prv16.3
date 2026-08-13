import CardLink2 from "../components/card-link2";
import { CardLink2_cids } from "../_cids";
import { CardLink2_styles } from "../_styles";
import { cardLink2Data as cardLink2DataContent } from "../content";
/** Automations section. */
export default function AutomationsSection({ cardLink2Data = cardLink2DataContent } = {}) {
  return (
    <div className="flex flex-col gap-4" data-cid="n142">
      <div className="flex flex-col gap-1" data-cid="n143">
        <h2 className="block text-color-001 text-xl font-semibold leading-7" data-cid="n144" data-component="heading">
          Automations
        </h2>
      </div>
      <div className="grid gap-4 grid-rows-[72px] grid-cols-3 max-md:grid-rows-[72px_72px_72px] max-md:grid-cols-1 md:max-lg:grid-rows-[72px_72px] md:max-lg:grid-cols-2" data-cid="n145">
        {cardLink2Data.map((d, i) => <CardLink2 key={i} d={d} cids={CardLink2_cids[i]} styles={CardLink2_styles[i]} />)}
      </div>
    </div>
  );
}
